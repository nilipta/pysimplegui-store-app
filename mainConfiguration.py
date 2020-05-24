from enum import Enum

popupPlace=(330, 250)
status_col_data_query = "SELECT locations,part_number,box_number,created_date,created_by FROM public.stock ORDER BY stock_id"
stock_table_all_data_query = "SELECT * FROM public.stock ORDER BY stock_id"

class SearchPattern(Enum):
    LOCATION = 1
    PARTNO = 2
    UNDEFINED = 3

class shouldUpdateOrInsert(Enum):
    INSERT = 1
    UPDATE = 2

