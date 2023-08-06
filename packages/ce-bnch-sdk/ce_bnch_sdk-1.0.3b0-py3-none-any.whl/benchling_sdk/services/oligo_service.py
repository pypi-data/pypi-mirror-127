from typing import Any, Dict, Iterable, List, Optional, Union

from benchling_api_client.api.oligos import (
    archive_oligos,
    bulk_create_oligos,
    bulk_get_oligos,
    create_oligo,
    get_oligo,
    list_oligos,
    unarchive_oligos,
    update_oligo,
)
from benchling_api_client.models.entity_archive_reason import EntityArchiveReason
from benchling_api_client.types import Response
from benchling_sdk.helpers.decorators import api_method
from benchling_sdk.helpers.logging_helpers import check_for_csv_bug_fix
from benchling_sdk.helpers.pagination_helpers import NextToken, PageIterator
from benchling_sdk.helpers.response_helpers import model_from_detailed
from benchling_sdk.helpers.serialization_helpers import (
    none_as_unset,
    optional_array_query_param,
    schema_fields_query_param,
)
from benchling_sdk.models import (
    AsyncTaskLink,
    DnaOligo,
    ListOligosSort,
    Oligo,
    OligoCreate,
    OligosArchivalChange,
    OligosArchive,
    OligosBulkCreateRequest,
    OligosPaginatedList,
    OligosUnarchive,
    OligoUpdate,
    RnaOligo,
)
from benchling_sdk.services.base_service import BaseService


class OligoService(BaseService):
    """
    Oligos.

    Oligos are short linear DNA sequences that can be attached as primers to full DNA sequences. Just like other
    entities, they support schemas, tags, and aliases.

    Please migrate to the corresponding DNA Oligos endpoints so that we can support RNA Oligos.

    See https://benchling.com/api/reference#/Oligos
    """

    @api_method
    def get_by_id(self, oligo_id: str) -> DnaOligo:
        """
        Get an Oligo by ID.

        See https://benchling.com/api/reference#/Oligos/getOligo
        """
        response = get_oligo.sync_detailed(client=self.client, oligo_id=oligo_id)
        return model_from_detailed(response)

    @api_method
    def _oligos_page(
        self,
        modified_at: Optional[str] = None,
        name: Optional[str] = None,
        bases: Optional[str] = None,
        folder_id: Optional[str] = None,
        mentioned_in: Optional[List[str]] = None,
        project_id: Optional[str] = None,
        registry_id: Optional[str] = None,
        schema_id: Optional[str] = None,
        archive_reason: Optional[str] = None,
        mentions: Optional[List[str]] = None,
        sort: Optional[ListOligosSort] = None,
        ids: Optional[Iterable[str]] = None,
        entity_registry_ids_any_of: Optional[Iterable[str]] = None,
        names_any_of: Optional[Iterable[str]] = None,
        schema_fields: Optional[Dict[str, Any]] = None,
        page_size: Optional[int] = None,
        next_token: NextToken = None,
    ) -> Response[OligosPaginatedList]:
        return list_oligos.sync_detailed(  # type: ignore
            client=self.client,
            modified_at=none_as_unset(modified_at),
            name=none_as_unset(name),
            bases=none_as_unset(bases),
            folder_id=none_as_unset(folder_id),
            mentioned_in=none_as_unset(optional_array_query_param(mentioned_in)),
            project_id=none_as_unset(project_id),
            registry_id=none_as_unset(registry_id),
            schema_id=none_as_unset(schema_id),
            archive_reason=none_as_unset(archive_reason),
            mentions=none_as_unset(optional_array_query_param(mentions)),
            sort=none_as_unset(sort),
            ids=none_as_unset(optional_array_query_param(ids)),
            entity_registry_idsany_of=none_as_unset(optional_array_query_param(entity_registry_ids_any_of)),
            namesany_of=none_as_unset(optional_array_query_param(names_any_of)),
            schema_fields=none_as_unset(schema_fields_query_param(schema_fields)),
            page_size=none_as_unset(page_size),
            next_token=none_as_unset(next_token),
        )

    def list(
        self,
        modified_at: Optional[str] = None,
        name: Optional[str] = None,
        bases: Optional[str] = None,
        folder_id: Optional[str] = None,
        mentioned_in: Optional[List[str]] = None,
        project_id: Optional[str] = None,
        registry_id: Optional[str] = None,
        schema_id: Optional[str] = None,
        archive_reason: Optional[str] = None,
        mentions: Optional[List[str]] = None,
        ids: Optional[Iterable[str]] = None,
        entity_registry_ids_any_of: Optional[Iterable[str]] = None,
        names_any_of: Optional[Iterable[str]] = None,
        schema_fields: Optional[Dict[str, Any]] = None,
        sort: Optional[ListOligosSort] = None,
        page_size: Optional[int] = None,
    ) -> PageIterator[Oligo]:
        """
        List Oligos.

        See https://benchling.com/api/reference#/Oligos/listOligos
        """
        check_for_csv_bug_fix("mentioned_in", mentioned_in)
        check_for_csv_bug_fix("mentions", mentions)

        def api_call(next_token: NextToken) -> Response[OligosPaginatedList]:
            return self._oligos_page(
                modified_at=modified_at,
                name=name,
                bases=bases,
                folder_id=folder_id,
                mentioned_in=mentioned_in,
                project_id=project_id,
                registry_id=registry_id,
                schema_id=schema_id,
                archive_reason=archive_reason,
                mentions=mentions,
                ids=ids,
                entity_registry_ids_any_of=entity_registry_ids_any_of,
                names_any_of=names_any_of,
                schema_fields=schema_fields,
                sort=sort,
                page_size=page_size,
                next_token=next_token,
            )

        def results_extractor(body: OligosPaginatedList) -> Optional[List[Oligo]]:
            return body.oligos

        return PageIterator(api_call, results_extractor)

    @api_method
    def create(self, oligo: OligoCreate) -> DnaOligo:
        """
        Create an Oligo.

        See https://benchling.com/api/reference#/Oligos/createOligo
        """
        response = create_oligo.sync_detailed(client=self.client, json_body=oligo)
        return model_from_detailed(response)

    @api_method
    def update(self, oligo_id: str, oligo: OligoUpdate) -> DnaOligo:
        """
        Update an Oligo.

        See https://benchling.com/api/reference#/Oligos/updateOligo
        """
        response = update_oligo.sync_detailed(client=self.client, oligo_id=oligo_id, json_body=oligo)
        return model_from_detailed(response)

    @api_method
    def archive(self, oligo_ids: Iterable[str], reason: EntityArchiveReason) -> OligosArchivalChange:
        """
        Archive Oligos.

        See https://benchling.com/api/reference#/Oligos/archiveOligos
        """
        archive_request = OligosArchive(reason=reason, oligo_ids=list(oligo_ids))
        response = archive_oligos.sync_detailed(client=self.client, json_body=archive_request)
        return model_from_detailed(response)

    @api_method
    def unarchive(self, oligo_ids: Iterable[str]) -> OligosArchivalChange:
        """
        Unarchive Oligos.

        See https://benchling.com/api/reference#/Oligos/unarchiveOligos
        """
        unarchive_request = OligosUnarchive(oligo_ids=list(oligo_ids))
        response = unarchive_oligos.sync_detailed(client=self.client, json_body=unarchive_request)
        return model_from_detailed(response)

    @api_method
    def bulk_get(self, oligo_ids: Iterable[str]) -> Optional[List[Union[DnaOligo, RnaOligo]]]:
        """
        Bulk get Oligos.

        See https://benchling.com/api/reference#/Oligos/bulkGetOligos
        """
        oligo_id_string = ",".join(oligo_ids)
        response = bulk_get_oligos.sync_detailed(client=self.client, oligo_ids=oligo_id_string)
        oligos_results = model_from_detailed(response)
        return oligos_results.oligos

    @api_method
    def bulk_create(self, oligos: Iterable[OligoCreate]) -> AsyncTaskLink:
        """
        Bulk create DNA Oligos.

        See https://benchling.com/api/reference#/Oligos/bulkCreateOligos
        """
        body = OligosBulkCreateRequest(list(oligos))
        response = bulk_create_oligos.sync_detailed(client=self.client, json_body=body)
        return model_from_detailed(response)
