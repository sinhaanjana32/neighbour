resource "azurerm_cosmosdb_account" "cosmos" {

  name                = var.cosmos_account_name

  resource_group_name = azurerm_resource_group.rg.name

  location            = azurerm_resource_group.rg.location

  offer_type          = "Standard"

  kind                = "MongoDB"

  consistency_policy {
    consistency_level = "Eventual"
  }

  geo_location {
    location          = azurerm_resource_group.rg.location
    failover_priority = 0
  }
}

resource "azurerm_cosmosdb_mongo_database" "neighborly" {

  name                = var.database_name

  resource_group_name = azurerm_resource_group.rg.name

  account_name        = azurerm_cosmosdb_account.cosmos.name
}

resource "azurerm_cosmosdb_mongo_collection" "advertisements" {

  name                = "advertisements"

  resource_group_name = azurerm_resource_group.rg.name

  account_name        = azurerm_cosmosdb_account.cosmos.name

  database_name       = azurerm_cosmosdb_mongo_database.neighborly.name

  shard_key           = "_id"

  throughput          = 400

  index {
    keys   = ["_id"]
    unique = true
  }
}

resource "azurerm_cosmosdb_mongo_collection" "posts" {

  name                = "posts"

  resource_group_name = azurerm_resource_group.rg.name

  account_name        = azurerm_cosmosdb_account.cosmos.name

  database_name       = azurerm_cosmosdb_mongo_database.neighborly.name

  shard_key           = "_id"

  throughput          = 400

  index {
    keys   = ["_id"]
    unique = true
  }
}