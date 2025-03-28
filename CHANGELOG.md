# CHANGELOG


## v0.2.0 (2025-03-28)

### Chores

- Bump fastapi-app version to 0.1.5
  ([`9b06b2f`](https://github.com/ucm-cse-prg/fastapi-app/commit/9b06b2fc9e8a30c3f09a32c09d6bc86a0127e87b))

### Features

- Add CORS middleware to FastAPI application
  ([`c531739`](https://github.com/ucm-cse-prg/fastapi-app/commit/c531739424f1111d65f724f8e7707cbee3e9e4e1))

- Add CSV loading for categories and products in test_api.py
  ([`ad7a7e8`](https://github.com/ucm-cse-prg/fastapi-app/commit/ad7a7e8c542e7b24b5432de503820b6d549a5f86))

### Refactoring

- Update Category and Product models
  ([`3aef355`](https://github.com/ucm-cse-prg/fastapi-app/commit/3aef355c7479c2ef3427cccaf73270b7b630f61e))

Updated Category and Product models to extend name and description length limits and allow
  additional characters

- Update CreateProductResponse to inherit from GetProductResponse
  ([`2f5d2f8`](https://github.com/ucm-cse-prg/fastapi-app/commit/2f5d2f8c80e903b2d9732693d4e0fac6fdf4f605))

- Update product retrieval to use Product object instead of ID
  ([`2e4e995`](https://github.com/ucm-cse-prg/fastapi-app/commit/2e4e995784b5c7a4ed2d884cfcd2f9de4613ac83))


## v0.1.5 (2025-03-12)

### Bug Fixes

- Update Docker image tags and README references to use the new repository name
  ([`d5d0884`](https://github.com/ucm-cse-prg/fastapi-app/commit/d5d0884842f301e83f17cb5cbc2627c898a13091))

### Documentation

- Update copilot instructions for commit messages
  ([`c994e91`](https://github.com/ucm-cse-prg/fastapi-app/commit/c994e9107337e985df50bdd6da2f78824a22f259))

This commit enhances the guidelines for writing commit messages, including format, structure, and
  examples.


## v0.1.4 (2025-03-10)

### Bug Fixes

- Update Docker image tags to use full registry path
  ([`5d4266f`](https://github.com/ucm-cse-prg/fastapi-app/commit/5d4266ff72520c373b98f58aa6ed19e5eea1f3aa))


## v0.1.3 (2025-03-10)

### Bug Fixes

- Update Docker tags to use dynamic output
  ([`30eaa8a`](https://github.com/ucm-cse-prg/fastapi-app/commit/30eaa8aff2a93604e9681a9834601a4301e4f5b9))


## v0.1.2 (2025-03-10)

### Bug Fixes

- Update Docker image tags in build workflow
  ([`0d7e9c9`](https://github.com/ucm-cse-prg/fastapi-app/commit/0d7e9c90c77b380d4e212c2ba84f15d507f7a556))


## v0.1.1 (2025-03-10)

### Bug Fixes

- Set environment variables for Docker registry
  ([`6646e55`](https://github.com/ucm-cse-prg/fastapi-app/commit/6646e55a3b766889a2f217d29664f588b7a880f3))


## v0.1.0 (2025-03-10)

### Bug Fixes

- Apply http_request_dependency to product retrieval function
  ([`5a77847`](https://github.com/ucm-cse-prg/fastapi-app/commit/5a778476d0bb118ed989a7dc02dee3919f7d1398))

- Change price field validator mode to 'after'
  ([`4cca471`](https://github.com/ucm-cse-prg/fastapi-app/commit/4cca471369dd0e22393c77b40862703ced998771))

- Update collection attribute to name in Product model
  ([`abdf72c`](https://github.com/ucm-cse-prg/fastapi-app/commit/abdf72ca2d36dea03903e4c465643392dd14c555))

- Updateproductrequest schema
  ([`c5175e4`](https://github.com/ucm-cse-prg/fastapi-app/commit/c5175e47e403132cbcd404ab020ead77393658c0))

The UpdateProductRequest schema was missing the custom price validation. This fix adds the custom
  price validation to the UpdateProductRequest schema by deriving the schema from Product model.

### Code Style

- Remove unused event_loop fixture from tests
  ([`dd94b50`](https://github.com/ucm-cse-prg/fastapi-app/commit/dd94b500557798b2de620f47e49f380b48ff6660))

### Continuous Integration

- Add Coveralls integration for test coverage reporting
  ([`386ec92`](https://github.com/ucm-cse-prg/fastapi-app/commit/386ec92741ab97da78deb232067cc433484bfee7))

- Add GitHub Actions workflows for build and test automation
  ([`92a1577`](https://github.com/ucm-cse-prg/fastapi-app/commit/92a1577c09498b3fc646524544a24d1ab7a805c8))

- Add linters and type checker to workflow
  ([`cfc075d`](https://github.com/ucm-cse-prg/fastapi-app/commit/cfc075da054c9d7b962c26e215afad3772fedc2d))

- Add MongoDB setup step in GitHub Actions workflow
  ([`e6d4f05`](https://github.com/ucm-cse-prg/fastapi-app/commit/e6d4f05d9de412697e612afff82e87df8b70a5f6))

- Configure Docker Compose for MongoDB service with network settings
  ([`7ba834c`](https://github.com/ucm-cse-prg/fastapi-app/commit/7ba834c8085d36962a875b84e8d446b178adecd7))

- Downgrade actions/checkout to v4 for stability
  ([`09bfed3`](https://github.com/ucm-cse-prg/fastapi-app/commit/09bfed31eb204abb60a1291f102f1981f15cbc92))

- Enhance GitHub Actions for Python and Docker releases
  ([`8580033`](https://github.com/ucm-cse-prg/fastapi-app/commit/8580033ce218a5211e60542842a144452db8d624))

- Updated workflow to include Python Semantic Release for versioning and tagging. - Added Docker
  image build and release steps. - Improved permissions and concurrency settings for better workflow
  management. - Updated dependencies in pyproject.toml for semantic release support.

- Update build command and remove unused dependency
  ([`52baa5f`](https://github.com/ucm-cse-prg/fastapi-app/commit/52baa5fec68849467d33de989b05f6e07861ff2e))

### Documentation

- Add coverage badge to README
  ([`ecbb5fa`](https://github.com/ucm-cse-prg/fastapi-app/commit/ecbb5fa0d4e752512fe9d6e081a2fec72c7fac39))

- Update README for clarity and structure
  ([`554bc53`](https://github.com/ucm-cse-prg/fastapi-app/commit/554bc53dc45d4a759ce8fd215572db8bd1484c21))

### Features

- Add error handling wrapper for action functions
  ([`15aca68`](https://github.com/ucm-cse-prg/fastapi-app/commit/15aca68f6ec97010c74f5f3d944091ba5d6332fe))

- Add functions to drop and close MongoDB connection
  ([`fde0920`](https://github.com/ucm-cse-prg/fastapi-app/commit/fde0920d71c12bc2afe94b6c1aaf860d0ac8ebf7))

- Enhance CLI options for FastAPI server with dynamic settings and additional parameters
  ([`bd2ae1d`](https://github.com/ucm-cse-prg/fastapi-app/commit/bd2ae1d919ea3ec0ec68d35f6a9b5ce2d68238db))

- Initialize FastAPI application with MongoDB integration and basic structure
  ([`869bc2b`](https://github.com/ucm-cse-prg/fastapi-app/commit/869bc2b5eb85535b1f9f867f0918760d90263026))

### Refactoring

- Add error handling for product retrieval and creation
  ([`4c74b89`](https://github.com/ucm-cse-prg/fastapi-app/commit/4c74b898200d4109074c627b874f5de1770495be))

- Enhance APIException logging and remove unused classes
  ([`0622d66`](https://github.com/ucm-cse-prg/fastapi-app/commit/0622d6655350b183c311efee0424bb6c4f541307))

- Improve product tests and add new cases
  ([`78ddc5f`](https://github.com/ucm-cse-prg/fastapi-app/commit/78ddc5fb9d7510b606cdfac6b564ae22ddfe0e15))

- Remove debug print statements from MongoDB initialization
  ([`59c70eb`](https://github.com/ucm-cse-prg/fastapi-app/commit/59c70ebbfb0d4a3d1af3133b73778055c98a6070))

- Remove unused default settings test cases
  ([`e6c830d`](https://github.com/ucm-cse-prg/fastapi-app/commit/e6c830dcc1b25bf3e6016f8e173cdff2c0f7a56e))

### Testing

- Add unit tests for settings configuration
  ([`531eb97`](https://github.com/ucm-cse-prg/fastapi-app/commit/531eb97a2766294a43976bee906775edce8c68fa))
