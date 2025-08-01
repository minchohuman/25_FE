import streamlit as st
import pandas as pd
import time

# 페이지 설정
st.set_page_config(
    page_title='LLM 기반 슬로우 쿼리 분석 및 튜닝 가이드 Agent',
    layout='wide'
)

# 전역 CSS: 입력창과 버튼 높이 및 라인 높이 맞추기
st.markdown(
    '''
    <style>
    /* 텍스트 입력창 높이 */
    [data-testid="stTextInput"] input {
        height: 42px !important;
    }
    /* 모든 버튼 높이 및 라인 높이, 패딩 제거 */
    [data-testid="stButton"] button {
        height: 42px !important;
        line-height: 42px !important;
        padding-top: 0 !important;
        padding-bottom: 0 !important;
    }
    </style>
    ''',
    unsafe_allow_html=True
)

# 헤더 영역
st.markdown(
    "<h2 style='background-color: #808080; color: white; padding: 10px; text-align: center;'>"
    "LLM 기반 슬로우 쿼리 분석 및 튜닝 가이드 Agent</h2>",
    unsafe_allow_html=True
)

# 업로드 영역
col1, col2 = st.columns(2)
with col1:
    db_file = st.file_uploader(
        label='Upload DB File here',
        type=['db', 'sqlite', 'sqlite3'],
        key='db_file'
    )
with col2:
    sql_file = st.file_uploader(
        label='Upload SQL file here',
        type=['sql', 'txt'],
        key='sql_file'
    )

# 분석 및 출력 영역 (하단 분할)
col3, col4 = st.columns([2, 1])

# 왼쪽: Slow log 출력
with col3:
    st.markdown(
        "<h3 style='background-color: #808080; color: white; padding: 10px; text-align: center; margin-top: 20px;'>"
        "Slow log 출력</h3>",
        unsafe_allow_html=True
    )
    log_placeholder = st.empty()
    if db_file:
        # TODO: 실제 slow log fetch 로직으로 교체
        while True:
            logs = "[예시] Slow query at {}".format(time.strftime('%Y-%m-%d %H:%M:%S'))
            log_placeholder.text(logs)
            time.sleep(5)
    else:
        st.info('DB 파일을 업로드해주세요.')

# 오른쪽: 사용자 입력 및 리포트
with col4:
    st.markdown(
        "<h3 style='background-color: #666666; color: white; padding: 10px; text-align: center; margin-top: 20px;'>"
        "분석 하고자 하는 로그 입력</h3>",
        unsafe_allow_html=True
    )
    # 키워드 입력 및 검색 버튼
    input_col, btn_col = st.columns([3, 1])
    with input_col:
        filter_text = st.text_input('키워드를 입력하세요', '')
    with btn_col:
        # 검색 버튼 위치 조정을 위한 상단 여백
        st.markdown("<div style='margin-top: 25px;'></div>", unsafe_allow_html=True)
        if st.button('검색'):
            if filter_text:
                # TODO: filter_text 기반 검색 로직 구현
                st.success(f"'{filter_text}' 키워드로 검색 중입니다...")
            else:
                st.warning('검색할 키워드를 입력해주세요.')

    # 리포트 다운로드 / 출력 버튼 / 출력 버튼
    if st.button('Report 다운로드 / 출력'):
        if filter_text:
            # TODO: filter_text 기반 분석 및 보고서 생성 로직 구현
            st.info(f"'{filter_text}' 기반 보고서를 생성 중입니다...")
            # 예시: report = generate_report(db_file, filter_text)
            # st.download_button('Download Report', data=report, file_name='report.pdf')
        else:
            st.warning('분석할 키워드를 입력해주세요.')
