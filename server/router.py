from server.routers import user, personal, museum, excursion, ticket

routers = (user.router, personal.router, museum.router, excursion.router, ticket.router)
