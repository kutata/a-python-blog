% include tpls/inc/header.tpl title=title

<div class="content entry-list">

  <article>
    <h1><a href="{{url}}">{{title}}</a></h1>
    <div class="entry-tag">Posted @ {{ftime}}</div>
    <div class="entry-content">
      {{!content}}
    </div>
  </article>

  % if comment:
  <div class="comment">
    <!-- Disqus Comment Start -->
    <div id="disqus_thread"></div>
    <script type="text/javascript">
        /* * * CONFIGURATION VARIABLES: EDIT BEFORE PASTING INTO YOUR WEBPAGE * * */
        var disqus_shortname = 'thxsme'; // required: replace example with your forum shortname

        /* * * DON'T EDIT BELOW THIS LINE * * */
        (function() {
            var dsq = document.createElement('script'); dsq.type = 'text/javascript'; dsq.async = true;
            dsq.src = '//' + disqus_shortname + '.disqus.com/embed.js';
            (document.getElementsByTagName('head')[0] || document.getElementsByTagName('body')[0]).appendChild(dsq);
        })();
    </script>
    <noscript>Please enable JavaScript to view the <a href="http://disqus.com/?ref_noscript">comments powered by Disqus.</a></noscript>
    <a href="http://disqus.com" class="dsq-brlink">comments powered by <span class="logo-disqus">Disqus</span></a>
    <!-- Disqus Comment End -->
  </div>
  % end
</div>

% include tpls/inc/second.tpl

<div class="clear"></div>

% include tpls/inc/footer.tpl online=online
