from database_connect_sql import rest_db_sql
from sqlalchemy.orm import sessionmaker
from database_connect_sql import engine
from scrapping import scrapping_image_from_google
from selenium import webdriver


Session = sessionmaker(bind=engine)
session = Session()

def request_from_sql():

    requests = session.query(rest_db_sql).filter(rest_db_sql.readed=='false')
    
    for req in requests:

        if req is not  None :

            try:
                wd =  webdriver.Firefox()

                obj=scrapping_image_from_google

                urls=obj.get_images_url_from_google(wd,5,req.quantity,req.title)

                file_path=obj.download_image("imgs/", urls, req.title)

                wd.quit()
                req.readed=True
                session.commit()
                

            except Exception as e:
                print(f"error{e}")            
        
    
    session.close()


if __name__=="__main__":
    request_from_sql()