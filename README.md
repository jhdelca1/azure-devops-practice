# **Azure DevOps Practice: Infraestructura y Despliegue en Kubernetes**

Este proyecto implementa una infraestructura completa en **Azure** utilizando **Terraform**, **Ansible** y **Kubernetes (AKS)**. 
Se han desplegado múltiples aplicaciones con contenedores, incluyendo una con almacenamiento persistente.

## Objetivo del Proyecto**
El objetivo es automatizar el despliegue de infraestructura en **Azure** y gestionar aplicaciones en **Kubernetes (AKS)** con prácticas DevOps. 

Se han utilizado las siguientes herramientas:
- **Terraform** para crear la infraestructura en Azure.
- **Ansible** para automatizar la configuración y despliegue de servicios.
- **Kubernetes (AKS)** para ejecutar aplicaciones en contenedores.
- **Azure Container Registry (ACR)** para el almacenamiento de imágenes Docker.
- **Podman** para gestionar contenedores en una máquina virtual de Azure.

## Estructura del Repositorio**

azure-devops-practice/
│── ansible/                  # Playbooks de Ansible
│   ├── inventory
│   ├── playbook.yml
│   ├── roles/kubernetes/
│   │   ├── tasks/main.yml
│   │   ├── templates/
│   │   │   ├── deployment.yaml.j2
│   │   │   ├── service.yaml.j2
│── app-persistente/          # Aplicación Flask con almacenamiento persistente
│   ├── Dockerfile
│   ├── app.py
│   ├── requirements.txt
│── kubernetes/               # Manifiestos de Kubernetes
│   ├── deployment/
│   │   ├── deployment.yaml
│   │   ├── deployment-app-persistente.yaml
│   ├── service/
│   │   ├── service.yaml
│   │   ├── service-app-persistente.yaml
│   ├── storage/
│   │   ├── pv.yaml
│   │   ├── pvc.yaml
│── terraform/                # Código de infraestructura en Azure
│   ├── main.tf
│   ├── aks.tf
│   ├── vm.tf
│── README.md  ←  Explicación detallada del proyecto
```

---

## Despliegue de la Infraestructura**

    ##Configurar Terraform y desplegar infraestructura en Azure**

      cd terraform
      terraform init
      terraform apply -auto-approve

      Esto creará los siguientes recursos en Azure:
        **Azure Kubernetes Service (AKS)**
        **Azure Container Registry (ACR)**
        **Máquina Virtual (VM) con Podman**
        **Grupo de Recursos y Redes**


    ### Configuración de Ansible y despliegue en AKS**

      cd ansible
      ansible-playbook -i inventory playbook.yml

      Esto aplicará los manifiestos de Kubernetes para:
        **Desplegar la aplicación Flask** en Kubernetes.
        **Configurar almacenamiento persistente en AKS**.
        **Exponer los servicios con LoadBalancer**.

    ### Validaciones en Kubernetes**

      kubectl get pods
      kubectl get svc

      Esto permite verificar que los pods y servicios estén correctamente ejecutándose.

    Para probar la aplicación Flask con almacenamiento persistente:

    curl -X POST http://<EXTERNAL-IP> -H "Content-Type: application/json" -d '{"text": "Hola desde Kubernetes"}'

    Luego, recuperamos los datos almacenados:

    curl -X GET http://<EXTERNAL-IP>

    **Si los datos persisten tras reiniciar el pod, la configuración es correcta.**

## Problemas Encontrados y Soluciones**
| **Problema** | **Solución Aplicada** |
|-------------|------------------|
| Error de autenticación en ACR | `az acr login --name <nombre_acr>` |
| Límite de IPs en Azure | Eliminamos una IP y reasignamos LoadBalancer |
| Pod sin acceso a almacenamiento | Configuramos PersistentVolume y PersistentVolumeClaim |
| Error de permisos en Docker | Agregamos el usuario al grupo `docker` y reiniciamos la sesión |

---

## Conclusión**
Este proyecto demuestra una implementación completa de **DevOps en Azure**, incluyendo infraestructura, despliegue y persistencia de datos en Kubernetes.



