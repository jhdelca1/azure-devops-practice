variable "resource_group_name" {
  description = "Nombre del grupo de recursos"
  type        = string
  default     = "rg-devops-practice"
}

variable "location" {
  description = "Ubicación en Azure"
  type        = string
  default     = "West Europe"
}

variable "acr_name" {
  description = "Nombre del Azure Container Registry"
  type        = string
}


