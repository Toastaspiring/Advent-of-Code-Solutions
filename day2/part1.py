def solve_gift_shop():

    input_data = "18623-26004,226779-293422,65855-88510,868-1423,248115026-248337139,903911-926580,97-121,67636417-67796062,24-47,6968-10197,193-242,3769-5052,5140337-5233474,2894097247-2894150301,979582-1016336,502-646,9132195-9191022,266-378,58-91,736828-868857,622792-694076,6767592127-6767717303,2920-3656,8811329-8931031,107384-147042,941220-969217,3-17,360063-562672,7979763615-7979843972,1890-2660,23170346-23308802"

    ranges = input_data.split(',')
    total_invalid_sum = 0
    invalid_ids_found = []

    print(f"Checking {len(ranges)} ranges...")

    for r in ranges:
        start_str, end_str = r.split('-')
        start = int(start_str)
        end = int(end_str)


        for num in range(start, end + 1):
            s_num = str(num)
            length = len(s_num)


            if length % 2 == 0:
                mid = length // 2
                first_half = s_num[:mid]
                second_half = s_num[mid:]

                if first_half == second_half:
                    total_invalid_sum += num
                    invalid_ids_found.append(num)

    print(f"\nFound {len(invalid_ids_found)} invalid IDs.")

    print(f"Examples found: {invalid_ids_found[:5]} ...")
    
    print(f"\nTotal Sum of Invalid IDs: {total_invalid_sum}")

if __name__ == "__main__":
    solve_gift_shop()