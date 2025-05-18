# 🧰 Homelab Services Overview

This page lists the core services running in my self-hosted homelab environment. Each service is containerized (via Docker) and serves a specific role, from identity management and monitoring to development and continuous integration.

| 🧱 **Container**         | 📝 **Description**                                                                                       | 🔗 **Link**                                      |
|--------------------------|----------------------------------------------------------------------------------------------------------|--------------------------------------------------|
| **[Authentik](https://github.com/ttesfazion/homelab/tree/main/docker/authentik)**           | Identity provider offering Single Sign-On (SSO) and authentication flows for self-hosted apps.             | [GitHub](https://github.com/goauthentik/authentik) |
| **Portainer**             | Web-based Docker management UI to deploy and monitor containers, volumes, networks, and stacks.            | [GitHub](https://github.com/portainer/portainer)   |
| **[Nginx Proxy Manager](https://github.com/ttesfazion/homelab/tree/main/docker/nginxproxymanager)** | Reverse proxy with SSL certificate management and an intuitive UI for exposing services securely. | [GitHub](https://github.com/NginxProxyManager/nginx-proxy-manager) |
| **[Uptime Kuma](https://github.com/ttesfazion/homelab/tree/main/docker/uptimekuma)**          | Self-hosted uptime monitoring tool with a clean dashboard and notification support.                         | [GitHub](https://github.com/louislam/uptime-kuma)  |
| **[Glance](https://github.com/ttesfazion/homelab/tree/main/docker/glance)**                 | Lightweight dashboard to access and organize local services from a central portal.                          | [GitHub](https://github.com/glancesapp/glances)    |
| **[Pi-hole](https://github.com/ttesfazion/homelab/tree/main/docker/pihole)**                   | DNS-level ad blocker for the whole network, with a web UI to control domain filtering.                      | [GitHub](https://github.com/pi-hole/pi-hole)       |
| **Jenkins**                 | Automation server for CI/CD pipelines, used to build, test, and deploy code.                                | [GitHub](https://github.com/jenkinsci/jenkins)     |
| **[Watchtower](https://github.com/ttesfazion/homelab/tree/main/docker/watchtower)**          | Automatically monitors and updates Docker containers to the latest image version.                           | [GitHub](https://github.com/containrrr/watchtower) |
| **[Code-Server](https://github.com/ttesfazion/homelab/tree/main/docker/codeserver)**             | VS Code running in the browser, ideal for remote development and lightweight IDE use.                       | [GitHub](https://github.com/coder/code-server)     |
| **[Ntfy](https://github.com/ttesfazion/homelab/tree/main/docker/ntfy)**                   | HTTP-based pub/sub notification system that supports push notifications to browsers and devices.            | [GitHub](https://github.com/binwiederhier/ntfy)    |

---

## 📌 Usage Tips

- Use **Authentik** to integrate SSO with apps like Portainer, Uptime Kuma, and Code-Server.
- Secure your external access using **Nginx Proxy Manager** with SSL certificates via Let's Encrypt.
- Keep everything up-to-date with **Watchtower**, but monitor for breaking changes in container images.
- Pair **Ntfy** with your scripts or services (like Jenkins or Uptime Kuma) to get real-time alerts.

---
