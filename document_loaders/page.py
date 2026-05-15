from langchain_community.document_loaders import WebBaseLoader
url="https://www.apple.com/in/macbook-pro/?afid=p240%7Cgo~cmp-11180744360~adg-113271656527~ad-784707910013_kwd-987394769~dev-c~ext-~prd-~mca-~nt-search&cid=aos-in-kwgo-txt-mac-mac--"
docs=WebBaseLoader(url).load()
print(docs[0].page_content)

