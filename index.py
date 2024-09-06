
    setup = component.get("setup", 0)
    ciclo = component.get("ciclo", 0)
    quantidade = component.get("quantidade", 1)
    sub_components = component.get("componentes", [])

    timeline = []
    start_time = current_time

    # Tempo de setup
    setup_end = start_time + setup
    timeline.append({'event': 'Setup', 'start': start_time, 'end': setup_end})
    start_time = setup_end

    # Tempo de ciclo
    cycle_end = start_time + ciclo
    timeline.append({'event': 'Cycle', 'start': start_time, 'end': cycle_end})
    start_time = cycle_end

    # Processar cada subcomponente
    for _ in range(quantidade):
        for sub_component in sub_components:
            for sub_component_name, sub_component_details in sub_component.items():
                sub_component_timeline = calculate_processing_times(sub_component_details, start_time)
                timeline.extend(sub_component_timeline)
                if sub_component_timeline:
                    start_time = sub_component_timeline[-1]['end']

    return timeline

# Carregar os componentes do arquivo JSON
components = load_components('process_components.json')

# Calcular e imprimir os tempos de processamento para o componente principal
main_component = components["cama-fulano-branco"]
timeline = calculate_processing_times(main_component)

print('Timeline of Operations:')
for event in timeline:
    print(f"Event: {event['event']}, Start: {event['start']}s, End: {event['end']}s")