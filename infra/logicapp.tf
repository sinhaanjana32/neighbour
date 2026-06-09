resource "azurerm_logic_app_workflow" "neighborly" {

  name                = "neighborly-logic-app"

  location            = azurerm_resource_group.rg.location

  resource_group_name = azurerm_resource_group.rg.name
}