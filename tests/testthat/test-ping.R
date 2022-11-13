test_that("multiplication works", {
  res <- ghactions::ping()
  expect_true(c('result') %in% names(res))
})

test_that("create organization", {
  res <- ghactions::create_org()
  expect_equal(res$name, "ckanr_test_org")
})
