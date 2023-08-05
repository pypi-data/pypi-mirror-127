from dataclasses import dataclass
from typing import TYPE_CHECKING, List

from ...naming import NamespaceMetadataPaths
from .atoms import NS_ATOM_TYPE, CompositeType, EntityClass, Table
from .feature_types import ANY_FEATURE_TYPE
from .load_util import dump_atom_list_to_dict, load_atom_dict_to_list
from .namespaced_id import NamespacedId

if TYPE_CHECKING:
    from .artifact_metadata import ArtifactMetadata  # pragma: no cover


@dataclass
class NamespaceMetadata:
    """full spec of metadata for a namespace"""

    composite_types: List[CompositeType]
    entity_classes: List[EntityClass]
    tables: List[Table]
    local_name: str

    def get(self, obj_id: str) -> NS_ATOM_TYPE:
        for atom in self._atoms:
            if atom.name == obj_id:
                return atom
        raise KeyError(f"{obj_id} not found in: \n {self}")

    def get_full(self, ns_id: NamespacedId, parent: "ArtifactMetadata"):
        if ns_id.is_local:
            return self.get(ns_id.obj_id)
        return parent.get_atom(ns_id)

    @classmethod
    def load_serialized(cls, subdir="") -> "NamespaceMetadata":
        ns_paths = NamespaceMetadataPaths(subdir)
        return cls(
            composite_types=load_atom_dict_to_list(
                ns_paths.composite_types, CompositeType
            ),
            entity_classes=load_atom_dict_to_list(
                ns_paths.entity_classes, EntityClass
            ),
            tables=load_atom_dict_to_list(ns_paths.table_schemas, Table),
            local_name=subdir,
        )

    def dump(self):
        ns_paths = NamespaceMetadataPaths(self.local_name, mkdir=True)
        for path, atom_list in [
            (ns_paths.table_schemas, self.tables),
            (ns_paths.entity_classes, self.entity_classes),
            (ns_paths.composite_types, self.composite_types),
        ]:
            dump_atom_list_to_dict(path, atom_list)

    @property
    def used_prefixes(self) -> List[str]:
        full_feature_list: List[ANY_FEATURE_TYPE] = []
        ns_ids = []
        for table in self.tables:
            full_feature_list += table.features + (table.index or [])
            ns_ids.append(table.subject_of_records.ns_prefix)

        for ct in self.composite_types:
            full_feature_list += ct.features

        for ec in self.entity_classes:
            for ecp in ec.parents or []:
                ns_ids.append(ecp.ns_prefix)

        full_ns_id_list = [
            feat.val_id.ns_prefix for feat in full_feature_list
        ] + ns_ids

        return list(set(filter(None, full_ns_id_list)))

    @property
    def _atoms(self) -> List[NS_ATOM_TYPE]:
        return [*self.composite_types, *self.entity_classes, *self.tables]
