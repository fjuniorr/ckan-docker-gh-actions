test_that("multiplication works", {
  res <- ghactions::ping()
  expect_equal(names(res), c("db", "redis", "solr"))
})
