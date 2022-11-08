test_that("multiplication works", {
  res <- ghactions::ping()
  expect_true(c('result') %in%% names(res))
})
