This branch shows the display of mock data on a product page.

To reproduce, 

1) minikube start
2) skaffold dev
3) kubectl port-forward deployment/frontend 8080:8080
4) localhost:8080 in Browser to open the shop

Display of reviews on this branch were achieved by adding a new review.html template,
by adjusting the product.html and by adjusting the productHandler() 
in handlers.go file.
