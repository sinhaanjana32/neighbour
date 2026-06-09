output "function_app_name" {
  value = azurerm_linux_function_app.function.name
}

output "function_url" {
  value = "https://${azurerm_linux_function_app.function.default_hostname}/api"
}

output "eventhub_connection_string" {

  sensitive = true

  value = azurerm_eventhub_authorization_rule.neighborly.primary_connection_string
}