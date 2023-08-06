💿 批量导入 geojson  (shpfile todo) 到 postgresql

Params:

- db_config: {
  "DB_USER": ""
  "DB_PASSWORD": ""
  "DB_HOST": ""
  "DB_PORT": ""
  "DB_NAME": ""
  }

- static_path: 相对路径
- if_exists: 'fail' | 'replace' | 'append', geopandas 中的参数

:rocket: 简单 Demo

```python
from geodata2pg import main

if __name__ == '__main__':
    db_config = {
        "DB_USER": "postgres",
        "DB_PASSWORD": "1973",
        "DB_HOST": "localhost",
        "DB_PORT": "5433",
        "DB_NAME": "mapbox-api"
    }

    path = './static'

    main(db_config, path, 'replace')

```