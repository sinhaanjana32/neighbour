resource "azurerm_service_plan" "plan" {

  name                = "neighborly-plan"

  location            = azurerm_resource_group.rg.location

  resource_group_name = azurerm_resource_group.rg.name

  os_type             = "Linux"

  sku_name            = "Y1"
}



resource "azurerm_linux_function_app" "function" {

  name                = var.function_app_name

  location            = azurerm_resource_group.rg.location

  resource_group_name = azurerm_resource_group.rg.name

  service_plan_id     = azurerm_service_plan.plan.id

  storage_account_name = azurerm_storage_account.storage.name

  storage_account_access_key = azurerm_storage_account.storage.primary_access_key

  site_config {

    application_stack {
      python_version = "3.11"
    }

    application_insights_connection_string = azurerm_application_insights.appinsights.connection_string
  }

  app_settings = {

    FUNCTIONS_WORKER_RUNTIME = "python"

    WEBSITE_RUN_FROM_PACKAGE = "1"
  }
}