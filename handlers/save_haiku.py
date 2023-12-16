from db import purge_variants_except_of, retrieve_haiku_by


async def choose_haiku_variant(haiku_id: str, variant_id: str) -> dict:
    purge_variants_except_of(variant_id, haiku_id)
    haiku = retrieve_haiku_by(haiku_id)
    return {"id": haiku_id, "text": haiku["chosen"]}
