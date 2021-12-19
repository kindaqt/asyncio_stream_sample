import asyncio
import random
from datetime import datetime


async def run(
    total_files: int, 
    total_time: int,
):
    print(f'run: total_files="{total_files}" total_time="{total_time}"')

    # Open Connection
    print(f'run: openning connection...')
    reader, writer = await asyncio.open_connection('127.0.0.1', 8888, ssl=False)
    print(f'run: opened connection')

    print(f'run: creating tasks...')
    tasks = create_tasks(total_files, reader, writer)
    print(f'run: created tasks')

    print("run: tasks running...")
    await asyncio.gather(*tasks)
    print("run: tasks complete")
    
    print("run: closing connection...")
    writer.close()
    print("run: closed connection")


def create_tasks(
    total_files, 
    reader: asyncio.StreamReader, 
    writer: asyncio.StreamWriter,
    min_time_interval = 0.01,  # 0.01 seconds / 1 millisecond
    max_time_interval = 1,  # 1 second / second (600000/1000/60 = 10 minutes)
):
    print(f' create_tasks: status="in_progress"')

    tasks = []
    delay = 0.00
    for i in range(total_files):
        file_name = f'{i}.bin'
        random_interval = random.uniform(min_time_interval, max_time_interval)
        delay += random_interval

        print(f' create_tasks: msg="creating task" file_name={file_name}, random_interval={random_interval}, random_interval={random_interval}, delay={delay}')
        tasks.append(
            asyncio.ensure_future(
                task(file_name, delay, reader, writer)
            )
        )
        print(f' create_tasks: msg="created task" file_name={file_name}, random_interval={random_interval}, random_interval={random_interval}, delay={delay}')

    print(f' create_tasks: status="complete"')

    return tasks

async def task(
    file_name: str, 
    delay: float,
    reader, 
    writer
):
    print(f'  task: status=in_progress file_name="{file_name}", delay={delay}, start_time={datetime.now().strftime("%H:%M:%S")}')

    # Wait to Run
    await asyncio.sleep(delay)

    # Generate Data
    file_data = create_data()
    
    # Create/Send File
    await asyncio.gather(
        send_data(reader, writer, file_data),
        create_file(file_name, file_data),
    )

    print(f'  task: status=complete file_name="{file_name}", delay={delay}, start_time={datetime.now().strftime("%H:%M:%S")}')


def create_data(    
    min_file_size = 2**10,  # 1024 B / 1 KB
    max_file_size = 2**20  # 1048576 B / 1 MB
) -> bytes:
    print(f"   create_data: status=in_progress")
    
    # Round to nearest even number since an int16 takes up 2 bytes
    size = random.randint(min_file_size, max_file_size)
    if size % 2:
        size += 1
    
    # Generate bytes of random int16s. range is size/2 because 2 bytes per are needed for every int16
    data: bytes = bytearray()
    for _ in range(round(size/2)):
        data += random.getrandbits(16).to_bytes(2, byteorder='big')

    print(f"   create_data: status=complete, size={size}, bytes_len={len(data)}")
    return data


async def create_file(file_name, file_data):
    print(f'   creating file: file_name={file_name}')
    
    size = 0
    with open(file_name, 'wb') as f:
        f.write(file_data)
        size = f.tell()

    print(f'   created file: file_name={file_name} size={size} bytes')


async def send_data(reader: asyncio.StreamReader, writer: asyncio.StreamWriter, file_data):
    print(f"   send_data: status=in_progress")

    # Send Data
    writer.write(file_data)
    await writer.drain()

    print(f"   send_data: status=complete")


def main():
    total_time = 600  # 600 seconds / 10 minutes
    total_files = 100  # 100 binary files

    loop = asyncio.get_event_loop()
    try:
        print("loop started")
        loop.run_until_complete(
            run(total_files, total_time)
        )
        print("loop completed")
    except Exception as e:
        print(f"loop error: error={e}")
    finally:
        print("loop closing")
        loop.close()
        print("loop closed")


if __name__ == '__main__':
    # Open Stream
    # Generate Files
    #     Generate File
    #     Stream File
    #     Delete File
    # Close Stream

    main()
