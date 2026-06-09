resource "azurerm_eventhub_namespace" "neighborly" {

  name                = "anjananeighborly-ehns"

  location            = azurerm_resource_group.rg.location

  resource_group_name = azurerm_resource_group.rg.name

  sku                 = "Standard"

  capacity            = 1
}

resource "azurerm_eventhub" "neighborly" {

  name                = "neighborly-events"

  namespace_id        = azurerm_eventhub_namespace.neighborly.id

  partition_count     = 2

  message_retention   = 1
}


resource "azurerm_eventhub_authorization_rule" "neighborly" {

  name           = "neighborly-policy"

  eventhub_name  = azurerm_eventhub.neighborly.name

  namespace_name = azurerm_eventhub_namespace.neighborly.name

  resource_group_name = azurerm_resource_group.rg.name

  listen = true

  send   = true

  manage = true
}