<div class="content entry-list">

<article>
  <h1>{{post['title']}}</h1>
  <div class="entry-tag">Posted @ {{post['date']}}</div>
  <div class="entry-content">
    % if post['preview']:
    <div class="entry-preview">
      {{! post['preview']}}
    </div>
    % else:
      {{! post['content']}}
    % end
  </div>
</article>

</div>

%rebase layout
