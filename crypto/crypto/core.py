import spiders
import filters

# if we separate the concerns of retrieving the main table
# and the relative info pages, than here a class will
# incapsulate the process. Otherwise a single spider will
# directly follow the refs (accumulating by a number that defaults to 5)
