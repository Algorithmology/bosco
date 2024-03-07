# bosco

```python
from pyinstrument import Profiler
from pyinstrument.renderers import JSONRenderer
profiler = Profiler()

profiler.start()
# do some work
profiler.stop()

print(JSONRenderer().render(profiler.last_session))
```
