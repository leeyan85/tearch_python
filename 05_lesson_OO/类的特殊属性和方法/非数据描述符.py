class Foo:
    def __get__(self, instance, owner):
        print('触发get')

    def __delete__(self, instance):
        print('触发delete')



