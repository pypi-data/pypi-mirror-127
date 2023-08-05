.. raw:: html

   <h1 id='0'>

fsm

.. raw:: html

   </h1>

`1. Introduction <#1>`__\  `2. Function introduction <#2>`__\  `    2.1.
Simplest example <#201>`__ `    2.2. Buffer mechanism <#202>`__ `   
2.3. Add documentation <#203>`__ `    2.4. Automatic data area <#204>`__
`    2.5. Transfer function priority <#205>`__ `    2.6. Manually
declare start and end points <#206>`__

    `back to vertex <#0>`__

    .. raw:: html

       <h2 id='1'> 

    1. Introduction

       .. raw:: html

          </h2> 

        A finite state machine written in pure python, perhaps I don't
       know whether it can be called a finite state machine. It realizes
       the function of finite state machine in a very simplified way.
       Perhaps it is more appropriate to call it easyfsm Due to the use
       of proxy, shelling and automatic simplification, it is slow. In
       terms of the time taken to loop 951600 times, this is 30 times
       slower than pure ordinary Python code (this ratio decreases with
       the increase of state logic complexity)

@Test

::

    from ezfsm import *
    import time
    tfs = [
        ["a", "b", lambda: True, lambda: ...]
    ]

    sm = StateMachine(tfs)  # You can also use SM instead of Statemachine

    # sm.EnableLogPrint(False)
    sm.EnableLogRecord(False)  # Turn off logging
    sm.Build()  # compile
    a = time.time()
    for i in range(921600):
        if (lambda : True)():
            (lambda : ...)()

    time1 = time.time() - a
    a += time1

    for i in range(921600):
        while not sm.IsFinish(): sm.Execute()  # You can also use sm() instead of sm.Execute()
        sm.Reset()
    time2 = time.time() - a

    print("传统耗时: %s, sm耗时: %s"%(time1, time2))

@run

::

    传统耗时: 0.34980034828186035, sm耗时: 10.96321439743042

The average additional cost of each operation is 10us. Those sensitive
to operation speed need to be considered carefully. At present, there is
no simplified version for micro python You can copy the code directly to
run on micro python, but the performance may be affected

    `back to vertex <#0>`__\ 

    .. raw:: html

       <h2 id='2'>

    2. Function introduction

       .. raw:: html

          </h2>

        The simplest way to use it will be introduced

    `back to vertex <#0>`__\ 

    .. raw:: html

       <h3 id='201'>

    2.1 The simplest example

    .. raw:: html

       </h3>

     Consider implementing a state machine with only (a, b) two states
    (as shown in the figure):

.. figure:: https://images.gitee.com/uploads/images/2021/1111/020337_92ddadc3_8637799.jpeg
   :alt: a to b.JPG

   输入图片说明
@example:

::

    from ezfsm import *    # This step is best to import all

    tfs = [
        ["a", "b", lambda: True, lambda: print("a -> b")]
    ]

    sm = StateMachine(tfs)    # You can also use SM instead of Statemachine

    sm.Build()    # compile


    #  Ususally, other general FSM does not need to be compiled
    #  But this step is set to standardize the data format and improve efficiency. It can make writing more convenient
    #  Statemachine without compilation cannot execute most operations.


    while not sm.IsFinish(): sm.Execute()    # You can also use sm() instead of sm.Execute()

    # if you want to view the graph, you must pip install graphviz and download the graphviz software. 

    graph = sm.StateGraph()    # get the graphviz.Digraph object
    graph.view()

--------------

@run<BR/>

::

    No set <start> <end>, Auto Set : {start <- a, end <- b}
    [Auto] Add srt<a> to state table.
    [Auto] Add dst<b> to state table.
    a -> b
    FSM Touch End<b>.

--------------

    \*In the above example, you only need to define a transfer function
    list (TFs) to fully describe the state machine (the rest of the code
    will not change with the complexity of the state machine)

    \*The basic operation principle of this state machine only includes
    state sets and transfer functions

    \*The state machine runs from a start point and checks whether each
    transition function executing the state is available according to a
    certain priority (it will be considered available if it returns true
    by calling a conditional function (cond\_func). Once a transfer
    function is considered available, the program will try to 'transfer'
    to the state pointed to by the transfer function and give up
    checking the remaining transfer functions, and 'transfer' is
    equivalent to calling the operation function (exec\_func).
    Therefore, a transfer function includes at least SRT, DST and cond\_
    func, exec\_ Func these four items of information are the necessary
    parameters for constructing the transfer function

    *If a state machine has only a transfer function as its parameter,
    it will try to automatically extract statesets, start, end *\ The
    above description can be written as follows:

::

    tfs = [
        TF("a", "b", lambda: True, lambda: print("a -> b")),  # TransFunc - TF
    ]

--------------

    `back to vertex <#0>`__\ 

    .. raw:: html

       <h3 id='202'>

    2.2 Buffer mechanism

    .. raw:: html

       </h3>

     You can set the number of buffering times, which can simply
    suppress the error trigger caused by overly sensitive conditions.
    Buffering n times can be understood as: n times pass (cond\_func)
    and cannot perform the 'transfer' operation. The transfer is not
    performed until the buffering is enough n times

::

    tfs = [
        ["a", "b", lambda: True, lambda: print("a -> b"), BufTs(3), BufDo(lambda: print("缓冲中."))]  # BufTs = BufTimes
    ]

@run

::

    No set <start> <end>, Auto Set : {start <- a, end <- b}
    [Auto] Add srt<a> to state table.
    [Auto] Add dst<b> to state table.
    缓冲中.
    缓冲中.
    缓冲中.
    a -> b
    FSM Touch End<b>.

|输入图片说明| >There are several points to note about buffering:
>>buffer: >> When the condition check of if passes, the status
opportunity attempts to perform the transfer operation >> However, if
there are n buffers, the state machine is reducing N by 1. And the
transfer operation is not performed until n < = 0 >> The following
actions will cause n to be reset: >>     1.After n times of buffering
and transfer operation >>     2.The transfer operation of another branch
of the state is performed >>     3.Reset by StateMachine.ResetBuffer > >
\*\*\* >\ `back to vertex <#0>`__\  >

.. raw:: html

   <h3 id='203'>

2.3 Add documentation

.. raw:: html

   </h3>

 >You can add documentation for the if do buf three parts of the
transfer function. This will not have any impact on the operation of the
program, but it will help you analyze the state diagram >It can be added
through the tfkwargs class or the key value pair passed into the TF
constructor:

::

    tfs = [
        ["a", "b", lambda: True, lambda: print("a -> b"),
         IfDoc("条件恒为True"), DoDoc("啥也不做."),
         BufTs(3), BufDo(lambda: print("缓冲中.")), BufDoc("缓冲3次.")]
    ]

    OR

    tfs = [
        TF("a", "b", lambda: True, lambda: print("a -> b"),
         cond_doc="条件恒为True", exec_doc="啥也不做.",
         buffer_times=3, buffer_exec=lambda: print("缓冲中."), buffer_doc="缓冲3次.")
    ]

|输入图片说明| \*\*\* >\ `back to vertex <#0>`__\  >

.. raw:: html

   <h3 id='204'>

2.4 Automatic data area

.. raw:: html

   </h3>

 >FSM provides a dataarea class. Except for the three names [set, Iadd,
isub], users can add their own attributes to it, so that they can be
used where needed。

::

    class DataArea(object):
        def iadd(self, attr, value):
            new = getattr(self, attr) + value
            setattr(self, attr, new)
            return new

        def isub(self, attr, value):
            new = getattr(self, attr) - value
            setattr(self, attr, new)
            return new

        def set(self, attr, value):
            setattr(self, attr, value)

    \*Another important feature is the four global data area variables:
    mach, Inst, DeST and this. Four dataarea proxy variables are built
    in FSM to make it easier for programmers to use cond\_ func、exec\_
    func、buffer\_ Func uses these four data areas in these three
    functions. It is called ** Auto ** data area because FSM will
    automatically determine the values of these data areas when
    executing specific transfer functions. The specific values are as
    follows: > mach: The running environment of the currently running
    state machine > inst: Running environment of current status node
    > dest: Running environment of target state node > this: The running
    environment of the transfer function itself

    @Example

::

    tfs = [
        # in -> a
        ['in', 'a', lambda :True,
            lambda :[print("进入状态机."), dest.set("left", 4)],  # in -> a, 所以dest为a的数据域
            DoDoc("设置a.left为4")],
        # a -> b
        ['a', 'b', lambda : inst.left <= 0,  # a -> b, 所以inst为a的数据域
            lambda :print("进入状态b."),
            IfDoc("a.left为0时")],
        # a -> a
        ['a', 'a', lambda : inst.left > 0,  # a -> b, 所以inst为a的数据域
            lambda :[print("进入状态a. left:", inst.left)  , inst.set('left', inst.left - 1)],  # a -> b, 所以inst为a的数据域
            IfDoc("a.left大于0时"),
            DoDoc("a.left--")],
        # b -> out
        ['b', 'out',
            lambda :True,
            lambda :print("进入状态out."),
            DoDoc("结束状态机")],
    ]

|输入图片说明| @run

::

    No set <start> <end>, Auto Set : {start <- in, end <- out}
    [Auto] Add srt<in> to state table.
    [Auto] Add dst<a> to state table.
    [Auto] Add dst<b> to state table.
    [Auto] Add dst<out> to state table.
    进入状态机.
    进入状态a. left: 4
    进入状态a. left: 3
    进入状态a. left: 2
    进入状态a. left: 1
    进入状态b.
    进入状态out.
    FSM Touch End<out>.

--------------

    `back to vertex <#0>`__\ 

    .. raw:: html

       <h3 id=205>

    2.5 Transfer function priority<3> When several state functions
    originate from the same state node, the order of state machine
    executing state functions needs to be studied The default priority
    is 0. FSM checks and executes all transfer functions under the same
    priority according to the principle of first in, first out

::

    tfs = [
        ["a", "b", lambda: True, lambda: print("a -> b, 1 channel")],  # First in, first out
        ["a", "b", lambda: True, lambda: print("a -> b, 2 channel")],  # The previous one is preferentially checked if it cond_ Func returns true, so it can't be executed here
    ]

@run

::

    No set <start> <end>, Auto Set : {start <- a, end <- b}
    [Auto] Add srt<a> to state table.
    [Auto] Add dst<b> to state table.
    a -> b, 1 channel
    FSM Touch End<b>.

    The way to modify the priority is to set it at the fifth data item:

::

    tfs = [
        ["a", "b", lambda: True, lambda: print("a -> b, 1 channel")],  # 优先级默认为0
        ["a", "b", lambda: True, lambda: print("a -> b, 2 channel"), 1],  # 优先级1优先于0检查
    ]

@run

::

    No set <start> <end>, Auto Set : {start <- a, end <- b}
    [Auto] Add srt<a> to state table.
    [Auto] Add dst<b> to state table.
    a -> b, 2 channel
    FSM Touch End<b>.

|输入图片说明| >

.. raw:: html

   <h2 id=206>

2.6 Manually declare start and end points

.. raw:: html

   </h2>

 >A simple state diagram can easily and automatically identify the
starting point and end point. Once the logic of nesting and loop occurs,
the system can not correctly identify the starting point and end point.
At this time, we need to specify it manually >The first way is to
specify directly when instantiating

::

    sm = SM(tfs, start='a', end='b')

    Another way is to use the Statemachine. Config () method to modify
    the start and end points

::

    sm.Config(start='a', end='b')

    If you pass in statesets, SM will preferentially select the
    beginning and end of state sets as start and end when it cannot find
    start and end

::

    states = ['a', 'b', 'c']
    tfs = [
        TF("a", "b", lambda: True, lambda: print("a -> b")),  # TransFunc - TF
        TF("b", "c", lambda: True, lambda: print("b -> c")),
        TF("b", "b", lambda: True, lambda: print("b -> b")), 
    ]
    sm = SM(states, tfs)  # If only TFs is transmitted, a logic error will occur (no error will be reported)

    It should be noted that the modified values have no effect before
    compilation, so you can modify them again before compilation

Software architecture
^^^^^^^^^^^^^^^^^^^^^

Installation tutorial
^^^^^^^^^^^^^^^^^^^^^

1. pip install ezfsm

instructions
^^^^^^^^^^^^

1. ::

       from ezfsm import *

2. 

.. |输入图片说明| image:: https://images.gitee.com/uploads/images/2021/1111/154244_b56d2f24_8637799.jpeg
.. |输入图片说明| image:: https://images.gitee.com/uploads/images/2021/1111/160605_7996e1e3_8637799.jpeg
.. |输入图片说明| image:: https://images.gitee.com/uploads/images/2021/1111/161923_0565aade_8637799.jpeg
.. |输入图片说明| image:: https://images.gitee.com/uploads/images/2021/1111/163753_f7e1306d_8637799.jpeg
