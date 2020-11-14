$(document).ready(function()
{
	$("#trending-next").click(function()
	{
		$(".trendingcardscrollpart")[0].scrollLeft+=820;
	})
	$("#trending-prev").click(function()
	{
		$(".trendingcardscrollpart")[0].scrollLeft-=820;
	})



	$("#diary-next").click(function()
	{
		$(".interesteddiariesscrollpart")[0].scrollLeft+=630;
	})
	$("#diary-prev").click(function()
	{
		$(".interesteddiariesscrollpart")[0].scrollLeft-=630;
	})



	$("#popular-next").click(function()
	{
		$(".interestedpopularscrollpart")[0].scrollLeft+=630;
	})
	$("#popular-prev").click(function()
	{
		$(".interestedpopularscrollpart")[0].scrollLeft-=630;
	})
})