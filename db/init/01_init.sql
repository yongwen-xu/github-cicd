CREATE TABLE hotel_plan (
    plan_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    prefecture_code VARCHAR(10) NOT NULL,
    hotel_name TEXT NOT NULL,
    plan_name TEXT NOT NULL,
    start_date DATE NOT NULL,
    end_date DATE NOT NULL,
    price INTEGER NOT NULL
);

INSERT INTO hotel_plan (prefecture_code, hotel_name, plan_name, start_date, end_date, price) VALUES 
('13', 'SUP5', 'スタンダードプラン', '2026-02-01', '2026-02-02', 20000),
('13', 'ピュトン東京', 'プレミアムルーム', '2026-02-01', '2026-02-02', 75000),
('27', 'サプホテル', 'デイユース', '2026-02-01', '2026-02-01', 4000),
('26', '井桁屋', '会合プラン', '2026-02-05', '2026-02-06', 50000),
('27', 'シングルトン大阪', 'デラックスルーム', '2026-03-01', '2026-03-02', 50000);