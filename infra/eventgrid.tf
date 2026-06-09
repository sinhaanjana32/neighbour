resource "azurerm_eventgrid_topic" "neighborly" {

  name = "anjanatopiclab1"

  location            = azurerm_resource_group.rg.location

  resource_group_name = azurerm_resource_group.rg.name

  input_schema        = "EventGridSchema"
}