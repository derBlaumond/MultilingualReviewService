# MultilingualReviewService

The repo has 4 "active" branches.

The "reviewservice" branch has the logic for the reviewservice backend logic and a short walkthrough.

Same goes for "translationservice.

The "frontend-integration" branch is our first attempt at rendering/displaying reviews on the product pages. 
We used mock data since the communication between review and frontend hasn't been established yet as of now.

"frontend-review-grpc" is our attempt at connecting the reviewservice with the frontend. 
It can be deployed the same way as "frontend-integration" with skaffold. We aren't using data from
the database since we can't submit to the database yet.
When trying to submit "HTTP Status: 500 Internal Server Error" should appear.
