% include public/tpls/inc/header.tpl title=title

<div class="content entry-list">
  % for k in postTime:
    % v=postList[k[1]]
<article>
  <h2><a href="{{v['url']}}">{{v['title']}}</a></h2>
  <div class="entry-tag">Posted @ {{v['ftime']}}</div>
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

% include public/tpls/inc/second.tpl

<div class="clear"></div>

%include public/tpls/inc/footer.tpl online=online
