from com.harrison.pubsub.example.PubSubImpl import PubSubImpl
from com.harrison.pubsub.example.StringData import StringData

test1 = PubSubImpl("test 1")

abc = "Hello World"

test2 = PubSubImpl("test 2")

test1.subscribe(str)
test2.subscribe(abc)

sd = StringData("This is some data")

test1.subscribe(StringData)
test2.subscribe(sd)

test1.publish(abc)
test2.publish(sd)
