def create_entity_type(project_id, display_name, kind):
    """Create an entity type with the given display name."""
    entity_types_client = dialogflow.EntityTypesClient()

    parent = entity_types_client.project_agent_path(project_id)
    entity_type = dialogflow.types.EntityType(
        display_name=display_name, kind=kind)

    response = entity_types_client.create_entity_type(parent, entity_type)

    print('Entity type created: \n{}'.format(response))

def delete_entity_type(project_id, entity_type_id):
    """Delete entity type with the given entity type name."""
    entity_types_client = dialogflow.EntityTypesClient()

    entity_type_path = entity_types_client.entity_type_path(
        project_id, entity_type_id)

    entity_types_client.delete_entity_type(entity_type_path)

def create_entity(project_id, entity_type_id, entity_value, synonyms):
    """Create an entity of the given entity type."""
    entity_types_client = dialogflow.EntityTypesClient()

    # Note: synonyms must be exactly [entity_value] if the
    # entity_type's kind is KIND_LIST
    synonyms = synonyms or [entity_value]

    entity_type_path = entity_types_client.entity_type_path(
        project_id, entity_type_id)

    entity = dialogflow.types.EntityType.Entity()
    entity.value = entity_value
    entity.synonyms.extend(synonyms)

    response = entity_types_client.batch_create_entities(
        entity_type_path, [entity])

    print('Entity created: {}'.format(response))

def delete_entity(project_id, entity_type_id, entity_value):
    """Delete entity with the given entity type and entity value."""
    entity_types_client = dialogflow.EntityTypesClient()

    entity_type_path = entity_types_client.entity_type_path(
        project_id, entity_type_id)

    entity_types_client.batch_delete_entities(
        entity_type_path, [entity_value])

def create_session_entity_type(project_id, session_id, entity_values,
                               entity_type_display_name, entity_override_mode):
    """Create a session entity type with the given display name."""
    session_entity_types_client = dialogflow.SessionEntityTypesClient()

    session_path = session_entity_types_client.session_path(
        project_id, session_id)
    session_entity_type_name = (
        session_entity_types_client.session_entity_type_path(
            project_id, session_id, entity_type_display_name))

    # Here we use the entity value as the only synonym.
    entities = [
        dialogflow.types.EntityType.Entity(value=value, synonyms=[value])
        for value in entity_values]
    session_entity_type = dialogflow.types.SessionEntityType(
        name=session_entity_type_name,
        entity_override_mode=entity_override_mode,
        entities=entities)

    response = session_entity_types_client.create_session_entity_type(
        session_path, session_entity_type)

    print('SessionEntityType created: \n\n{}'.format(response))

def delete_session_entity_type(project_id, session_id,
                               entity_type_display_name):
    """Delete session entity type with the given entity type display name."""
    session_entity_types_client = dialogflow.SessionEntityTypesClient()

    session_entity_type_name = (
        session_entity_types_client.session_entity_type_path(
            project_id, session_id, entity_type_display_name))

    session_entity_types_client.delete_session_entity_type(
        session_entity_type_name)
