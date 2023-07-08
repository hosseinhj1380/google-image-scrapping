
from selenium import webdriver
import base64
from selenium.webdriver.common.by import By
import requests
import io
from PIL import Image
import time
import os
# wd =  webdriver.Firefox()

class scrapping_image_from_google:

	def get_images_url_from_google(wd, delay, max_images,search_query):

		def scroll_down(wd):
			if max_images<400:
				wd.execute_script("window.scrollTo(0, document.body.scrollHeight);")
				time.sleep(delay)
			else:
				last_height = wd.execute_script('return document.body.scrollHeight')
				while True:
					wd.execute_script('window.scrollTo(0, document.body.scrollHeight)')
					time.sleep(delay)	
					new_height = wd.execute_script('return document.body.scrollHeight')

					try:
						element = wd.find_element(By.XPATH, "//input[@value='Show more results']")


						element.click()
						time.sleep(delay)
					except:
						pass
					if new_height == last_height:
						break
					last_height = new_height

		url = f"https://www.google.com/search?q={search_query}&tbm=isch"
		wd.get(url)

		image_urls = set()
		skips = 0
		scroll_down(wd)

		thumbnails = wd.find_elements(By.CLASS_NAME, "Q4LuWd")

		while len(image_urls) + skips < max_images:
			
			for img in thumbnails[len(image_urls) + skips:max_images]:
				
				try:
					img.click()
					time.sleep(delay)
				except:
					continue

				images = wd.find_elements(By.CLASS_NAME, "r48jcc")
				for image in images:
					if image.get_attribute('src') in image_urls:
						max_images += 1
						skips += 1
						break

					if image.get_attribute('src') and 'http' in image.get_attribute('src'):
						image_urls.add(image.get_attribute('src'))
						print(f"Found [{len(image_urls)}]")
		return image_urls
	def download_image(download_path, urls, file_name):
		result=[]
		main_directory=f"{download_path}/{file_name}"
		os.makedirs(main_directory)
		
		for i,  url in enumerate(urls):
		
			try:
				image_content = requests.get(url,allow_redirects=True,timeout=10).content
				image_file = io.BytesIO( image_content)
				image = Image.open(image_file)
				file_path = f"{main_directory}/{i+1}.jpeg"
				image = image.convert('RGB')

				with open(file_path, "wb") as f:
					image.save(f, "JPEG")

				print(f"Success download[{i+1}] ")
				result.append(file_path)

			except Exception as e:
				print('FAILED -', e)
		return(result)



if __name__=='__main__':

	obj=scrapping_image_from_google
	urls = obj.get_images_url_from_google(wd, 3, 3,search_query="mountain")
	obj.download_image("imgs/", urls, "mountain")
	wd.quit()