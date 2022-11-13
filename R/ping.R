#' Flatten resource
#'
#' Ping the flask web application.
#'
#' @param host path to a datapackage.json file
#' @param port base resource to flatten
#'
#' @examples
#' \dontrun{
#' ping()
#'
#' ping(host = "ckan")
#' }
#' @export
ping <- function(host = "localhost", port = "8000") {
  url <- glue::glue("http://{host}:{port}/api/3/action/status_show")
  res <- httr::GET(url)
  result = httr::content(res)
  print(result)
  result
}

#' @export
create_org <- function() {
  try(ckanr::organization_create(name = "ckanr_test_org",
                          title = "ckanr test org",
                          url = "http://localhost:5000",
                          key = Sys.getenv("TEST_API_KEY")),
      silent = TRUE)
  result <- ckanr::organization_show(url = "http://localhost:5000", id = "ckanr_test_org")
  result
}
