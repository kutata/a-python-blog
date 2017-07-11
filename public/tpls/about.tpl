%include public/tpls/inc/header.tpl title=title

<div class="content entry-list">
  <article>
    <div class="entry-content">
      <p>About.</p>
    </div>
  </article>

  % if comment:
    <!-- Disqus -->
  % end
</div>

%include public/tpls/inc/second.tpl

<div class="clear"></div>

%include public/tpls/inc/footer.tpl online=online
