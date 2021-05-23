# Algorytm-Kruskala

<a href="https://en.wikipedia.org/wiki/Kruskal%27s_algorithm">Wikipedia</a><br>
<a href="https://www.programiz.com/dsa/kruskal-algorithm"> Programiz info on the algorithm </a>
 
<pre><b>algorithm</b> Kruskal(<i>G</i>) <b>is</b>
    F:= ∅
    <b>for each</b> v ∈ G.V <b>do</b>
        MAKE-SET(v)
    <b>for each</b> (u, v) <b>in</b> G.E ordered by weight(u, v), increasing <b>do</b>
        <b>if</b> FIND-SET(u) ≠ FIND-SET(v) <b>then</b>
            F:= F ∪ {(u, v)} ∪ {(v, u)}
            UNION(FIND-SET(u), FIND-SET(v))
    <b>return</b> F
</pre>