# WikiMatcher
 Parses pages and returns simple objects to lookup/match against. It's loosely an in-memory database.

# Samples
	
## WikiMatcher
  This creates a matcher that will loosely match strings found in the wiki, created further below. We use the StrCloseComparer to allow for discrepencies in the search text. 
    matcher = WikiMatcher(StrCloseComparer(), BaseIgnorer, wiki, 0.9)

## ListIgnorer
  This ignores all instances of any phrase provided in the list.
	BaseIgnorer = ListIgnorer(['Director', 'Non-Canon Name'])

## Wiki
  This creates the wiki, searching all pages currently in it's internal list. This is appended to by the add_page function. Indexes are not created until the update function is called.
    wiki = Wiki()
    wiki.add_page(some_page)
	wiki.update()

## WikiPage
  This creates the page that can be searched through
    some_page = WikiPage('www.myfanwiki.com/wiki/Curse_of_Cannibal_Island/Actors', ActorParser(BaseIgnorer))

## WikiParser
 This is an abstract class, so each instance of this will be unique to your application. For Example:
 class ActorParser(WikiMatcher.wiki_parser.PageParser):
    def find_items(self, soup: BeautifulSoup)->ActorItems:
	    items = []
		for element in soup.findAll(ElementMatchPattern):
		    items.append(element)
		return items
	def create_item(self, data):
	    return ActorItem(data[0], data[2], int(data[1])) # Or Whatever formatting you need

## WikiItem
 These are what are found by matching against the WikiItem's key_names list. key_names should be unique, but this is not enforced. For example, the following will be searchable by the person's id, but not their non-unique name:
 
    class ActorItem(WikiItem):
        def __init__(self, name, person_id, age):
            super().__init__(name)
            self.person_id = person_id
            self.age = age
        
		def key_names(self):
			return [ f'actor {self.person_id}', f'actor #{self.person_id}', self.person_id ]