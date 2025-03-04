class ProxyManager:
    def __init__(self):
        self.proxies_per_email = 100
        self.proxy_map = {}

    def assign_proxy(self, email, proxy):
        if email not in self.proxy_map:
            self.proxy_map[email] = []
        if len(self.proxy_map[email]) < self.proxies_per_email:
            self.proxy_map[email].append(proxy)
            return f"Proxy {proxy} assigned to {email}."
        return f"Cannot assign more than {self.proxies_per_email} proxies to {email}."

    def get_status(self):
        status = "Proxy Status:\n"
        for email, proxies in self.proxy_map.items():
            status += f"{email}: {len(proxies)} proxies\n"
        return status
