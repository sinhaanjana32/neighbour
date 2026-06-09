resource "azurerm_kubernetes_cluster" "aks" {

  name                = "neighborlyaks"

  location            = azurerm_resource_group.rg.location

  resource_group_name = azurerm_resource_group.rg.name

  dns_prefix          = "neighborly"

  default_node_pool {

    name       = "default"

    node_count = 1

    vm_size    = "Standard_B2s"
  }

  identity {
    type = "SystemAssigned"
  }
}

resource "azurerm_role_assignment" "aks_acr" {

  principal_id = azurerm_kubernetes_cluster.aks.kubelet_identity[0].object_id

  role_definition_name = "AcrPull"

  scope = azurerm_container_registry.acr.id
}