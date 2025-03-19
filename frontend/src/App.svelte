<script>
    import { onMount } from "svelte";
    import * as echarts from "echarts";

    let data = null;

    onMount(async () => {
        try {
            const response = await fetch("http://localhost:8000/data");
            data = await response.json();
            console.log("Datos recibidos:", data);

            if (data) {
                drawPieChart();
                drawBarChart();
            }
        } catch (error) {
            console.error("Error al obtener los datos:", error);
        }
    });

    function drawPieChart() {
        let chartDom = document.getElementById("piechart");
        if (!chartDom) return;

        let myChart = echarts.init(chartDom);
        myChart.setOption({
            title: { text: "Distribución de Productos", left: "center" },
            tooltip: { trigger: "item" },
            legend: { bottom: 0 },
            series: [
                {
                    name: "Productos",
                    type: "pie",
                    radius: "50%",
                    data: data.piechart.labels.map((label, index) => ({
                        name: label,
                        value: data.piechart.values[index],
                    })),
                },
            ],
        });
    }

    function drawBarChart() {
        let chartDom = document.getElementById("barplot");
        if (!chartDom) return;

        let myChart = echarts.init(chartDom);
        myChart.setOption({
            title: { text: "Ventas Mensuales", left: "center" },
            tooltip: { trigger: "axis" },
            xAxis: { type: "category", data: data.barplot.categories },
            yAxis: { type: "value" },
            series: [{ data: data.barplot.values, type: "bar" }],
        });
    }
</script>

<h1>Gráficos con eCharts</h1>
<div style="display: flex; gap: 20px;">
    <div id="piechart" style="width: 400px; height: 300px;"></div>
    <div id="barplot" style="width: 400px; height: 300px;"></div>
</div>
