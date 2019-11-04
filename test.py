from attr import attrs, attrib

class MISSING:
    pass

class XMLNode:
    def to_xml_node():
        build_sub()

@attrs
class Order(XMLNode):
    a = attrib(MISSING)
    b = attrib(MISSING)
    order_lines = attrib(MISSING)

    def build_sub(self):
        order_lines = self.OrderLines(**self.order_lines)
        order_lines.build_sub()
    
    @attrs
    class OrderLines(XMLNode):
        order_line = attrib(MISSING)

        def build_sub(self):
            if self.order_line:
                for i in self.order_line:
                    order_line = self.OrderLine(**i)
                    order_line.build_sub()
              
        @attrs
        class OrderLine(XMLNode):
            item = attrib(MISSING)
            person = attrib(MISSING)

            def build_sub(self):
                item = self.Item(**self.item)
                item.build_sub()
                person = self.Person(**self.person)
                person.build_sub()
            
            @attrs
            class Item(XMLNode):
                c = attrib(MISSING)
                d = attrib(MISSING)

                def build_sub(self):
                    print(self.c, self.d)
            
            @attrs
            class Person(XMLNode):
                e = attrib(MISSING)

                def build_sub(self):
                    print(self.e)
                

def order():
    return {"a": 1, "b": 2, order_lines.__name__: order_lines()}

def order_lines():
    return {order_line.__name__: order_line()}

def order_line():
    return [{item.__name__: item(), person.__name__: person()}]

def item():
    return {"c": 3, "d": 4}

def person():
    return {"e": 5}

if __name__ == "__main__":
    dic = order()
    o = Order(**dic)
    o.build_sub()