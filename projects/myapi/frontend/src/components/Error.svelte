<script>
    export let error  
</script>

{#if typeof error.detail === 'string'}
<div class="alert alert-danger" role="alert">
    <div>
        {error.detail}
    </div>
</div>
    <ul>
        <li>{error.detail}</li>
    </ul>
{:else if typeof error.detail === 'object' && error.detail.length > 0 }
<div class="alert alert-danger" role="alert">
    {#each error.detail as err, i}
    <div>
        <strong>{err.loc[1]}</strong> : {err.msg}
    </div>
    {/each}
</div>
    <ul>
        {#each error.detail as err, i}
        <li>
            <strong>{err.loc[1]}</strong> : {err.msg}
        </li>
        {/each}
    </ul>
{/if}
