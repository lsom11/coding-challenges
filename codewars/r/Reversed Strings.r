solution <- function(s){
  splits <- strsplit(s, "")[[1]]
  reversed <- rev(splits)
  return(paste(reversed, collapse = ""))
}