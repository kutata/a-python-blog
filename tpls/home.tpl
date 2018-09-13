% include tpls/inc/header.tpl title=title

<div class="content entry-list">

% for v in posts:
  <article>
    <h1><a href="{{v['url']}}">{{v['title']}}</a></h1>
    <div class="entry-tag">Posted @ {{v['date']}}</div>
    <div class="entry-content">
      % if v['preview']:
      <div class="entry-preview">
        {{! v['preview']}}
      </div>
      % else:
        {{! v['content']}}
      % end
    </div>
  </article>
% end

</div>

% include tpls/inc/second.tpl

<div class="clear"></div>

%include tpls/inc/footer.tpl online=online
