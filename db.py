database: dict[str, dict] = {}  # TODO: replace with DynamoDB


def save_to_db(haiku_id: str, data: dict) -> None:
    database[haiku_id] = data
    print(database)


def purge_variants_except_of(variant_id: str, haiku_id: str):
    chosen = database[haiku_id]["haiku_variants"][variant_id]
    database[haiku_id]["chosen"] = chosen
    database[haiku_id].pop("haiku_variants")
    print(database)


def retrieve_haiku_by(haiku_id: str) -> dict:
    return database[haiku_id]
