```sql
-- ============================================
-- SHADOWNET CYBERSECURITY ANALYTICS QUERIES
-- ============================================


-- ============================================
-- 1. ATTACK TYPE ANALYSIS
-- ============================================

SELECT
    attack_type,
    COUNT(*) AS total_attacks
FROM firewall_logs
GROUP BY attack_type
ORDER BY total_attacks DESC;



-- ============================================
-- 2. THREAT LEVEL ANALYSIS
-- ============================================

SELECT
    threat_level,
    COUNT(*) AS total_threats
FROM firewall_logs
GROUP BY threat_level
ORDER BY total_threats DESC;



-- ============================================
-- 3. FAILED LOGIN DETECTION
-- ============================================

SELECT
    user_id,
    failed_attempts,
    login_location,
    device_type
FROM login_activity_logs
WHERE failed_attempts >= 3
ORDER BY failed_attempts DESC;



-- ============================================
-- 4. TOP ATTACK COUNTRIES
-- ============================================

SELECT
    country,
    COUNT(*) AS total_attacks
FROM firewall_logs
GROUP BY country
ORDER BY total_attacks DESC
LIMIT 10;



-- ============================================
-- 5. MOST TARGETED PORTS
-- ============================================

SELECT
    port_number,
    COUNT(*) AS total_attacks
FROM firewall_logs
GROUP BY port_number
ORDER BY total_attacks DESC
LIMIT 10;



-- ============================================
-- 6. ATTACK TREND ANALYSIS
-- ============================================

SELECT
    DATE(timestamp) AS attack_date,
    COUNT(*) AS total_attacks
FROM firewall_logs
GROUP BY attack_date
ORDER BY attack_date;



-- ============================================
-- 7. SUCCESS VS FAILED LOGINS
-- ============================================

SELECT
    login_status,
    COUNT(*) AS total_logins
FROM login_activity_logs
GROUP BY login_status;



-- ============================================
-- 8. MFA STATUS ANALYSIS
-- ============================================

SELECT
    mfa_status,
    COUNT(*) AS total_users
FROM login_activity_logs
GROUP BY mfa_status;



-- ============================================
-- 9. DEVICE TYPE ANALYSIS
-- ============================================

SELECT
    device_type,
    COUNT(*) AS total_devices
FROM login_activity_logs
GROUP BY device_type
ORDER BY total_devices DESC;



-- ============================================
-- 10. BROWSER USAGE ANALYSIS
-- ============================================

SELECT
    browser,
    COUNT(*) AS total_users
FROM login_activity_logs
GROUP BY browser
ORDER BY total_users DESC;



-- ============================================
-- 11. HIGH RISK ATTACKS ONLY
-- ============================================

SELECT
    *
FROM firewall_logs
WHERE threat_level IN ('High', 'Critical');



-- ============================================
-- 12. BLOCKED ATTACKS
-- ============================================

SELECT
    action_taken,
    COUNT(*) AS total_actions
FROM firewall_logs
GROUP BY action_taken;



-- ============================================
-- 13. ATTACKS BY PROTOCOL
-- ============================================

SELECT
    protocol,
    COUNT(*) AS total_attacks
FROM firewall_logs
GROUP BY protocol
ORDER BY total_attacks DESC;



-- ============================================
-- 14. DAILY FAILED LOGINS
-- ============================================

SELECT
    DATE(timestamp) AS login_date,
    COUNT(*) AS failed_logins
FROM login_activity_logs
WHERE login_status = 'Failed'
GROUP BY login_date
ORDER BY login_date;



-- ============================================
-- 15. TOP SUSPICIOUS USERS
-- ============================================

SELECT
    user_id,
    SUM(failed_attempts) AS total_failed_attempts
FROM login_activity_logs
GROUP BY user_id
ORDER BY total_failed_attempts DESC
LIMIT 10;
```
