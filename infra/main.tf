resource "azurerm_resource_group" "rg" {
  name     = var.resource_group_name
  location = var.location
}

resource "azurerm_storage_account" "storage" {
  name                     = var.storage_account_name

  resource_group_name      = azurerm_resource_group.rg.name

  location                 = azurerm_resource_group.rg.location

  account_tier             = "Standard"

  account_replication_type = "LRS"
}


resource "azurerm_application_insights" "appinsights" {

  name                = "neighborly-appinsights"

  location            = azurerm_resource_group.rg.location

  resource_group_name = azurerm_resource_group.rg.name

  application_type    = "web"
}