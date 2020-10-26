with counts as (
    select 
        (select count(*) from fb_search_results where position >= 3) as top_three_count,
        count(*) as total_count
    from fb_search_results
)
select (top_three_count * 100) / total_count as percent_top_three from counts