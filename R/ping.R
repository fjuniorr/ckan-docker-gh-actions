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